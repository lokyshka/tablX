package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"unicode/utf8"
)

var table [][]string

func askfile() *os.File {
	var path string

	fmt.Print("введите имя файла, включая его расширение: ")
	fmt.Scan(&path)

	supext := strings.HasSuffix(path, ".csv")

	if !supext {
		fmt.Println("tablX на данные момент поддерживает только .csv табилцы!")
		return nil
	}

	file, err := os.OpenFile(path, os.O_RDWR, 0666)
	if err != nil {
		fmt.Println("ошибка: не удалось открыть файл!")
		return nil
	}

	return file
}

func readtable(file *os.File) bool {
	var linenum uint

	// разбиваем текст на строки, а затем и на ячейки
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		table = append(table, strings.Split(line, ";"))
		linenum++
	}

	err := scanner.Err()
	if err != nil {
		fmt.Println("ошибка: не удалось прочитать файл.")
		return false
	}

	return true
}

func showtable() {
	var maxhdlen []int = make([]int, len(table[0]))
	var lenval int

	for ln := range len(table) {
		for hd := range len(table[ln]) {
			// если значение посередние — добавляем 2 пробела, если по краям — 1
			addval := 1
			if hd != 0 || hd != len(table[ln])-1 {
				addval++
			}

			lenval = utf8.RuneCountInString(table[ln][hd]) + addval
			if lenval > maxhdlen[hd] {
				maxhdlen[hd] = lenval
			}
		}
	}

	padspaces := func(val string, numspaces int) string {
		var b strings.Builder
		var cursidesp int
		b.Grow(len(val) + numspaces)

		// определяем кол-во пробелов слева и заполняем их
		cursidesp = numspaces / 2
		for range cursidesp {
			b.WriteByte(' ')
		}
		b.WriteString(val)

		// определяем кол-во пробелов слева
		cursidesp = numspaces / 2
		if numspaces%2 != 0 {
			cursidesp++
		}

		// заполняем пробелы справа
		for range cursidesp {
			b.WriteByte(' ')
		}
		return b.String()
	}

	for hd := range len(table[0]) {
		// вычисляем букву заголовка, находим кол-во пробелов по краям для ровной таблицы и заполняем их
		ch := 'A' + rune(hd)
		numspaces := maxhdlen[hd] - 1
		val := padspaces(string(ch), numspaces)

		// выводим
		if hd != 0 {
			fmt.Print("|")
		} else {
			// находим длину номера строки и отступа
			count := 3
			num := len(table) - 1
			for num > 0 {
				count++
				num /= 10
			}

			// делаем отступ
			var b strings.Builder
			b.Grow(count)
			for range count {
				b.WriteByte(' ')
			}
			fmt.Print(b.String())
		}
		fmt.Print(val)
		if hd == len(table[0])-1 {
			fmt.Println()
		}
	}

	for ln := range len(table) {
		for hd := range len(table[ln]) {
			var val string

			// находим кол-во пробелов по краям для ровной таблицы и заполняем их
			numspaces := maxhdlen[hd] - len(table[ln][hd])
			val = padspaces(table[ln][hd], numspaces)

			// выводим
			if hd != 0 {
				fmt.Print("|")
			} else {
				// находим текущую длину номера строки
				numlen := 0
				num := ln
				if num == 0 {
					numlen = 1
				}
				for num > 0 {
					numlen++
					num /= 10
				}

				// находим максимальную длину номера строки и отступа
				maxnumlen := 0
				num = len(table) - 1
				if num == 0 {
					numlen = 1
				}
				for num > 0 {
					maxnumlen++
					num /= 10
				}
				tablen := maxnumlen - numlen + 2

				// делаем отступ и номер строки
				var b strings.Builder
				b.Grow(tablen)
				b.WriteString(fmt.Sprint(ln))
				b.WriteByte(')')

				for range tablen {
					b.WriteByte(' ')
				}
				fmt.Print(b.String())
			}
			fmt.Print(val)
			if hd == len(table[ln])-1 {
				fmt.Println()
			}
		}
	}
}

func main() {
	var file *os.File
	for file == nil {
		file = askfile()
	}

	flag := readtable(file)
	if !flag {
		main()
		return
	}

	showtable()
}

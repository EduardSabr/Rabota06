from tkinter import *
# Функция для создания графического интерфейса
def num1():
    # Создаем основное окно
    window = Tk()
    numl = Label(window, text="Введите количество критериев:")
    numl.pack()
    numlentry = Entry(window)
    numlentry.pack()
    knopka = Button(window, text="Подтвердить", command=lambda: num2(window, int(numlentry.get())))
    knopka.pack()

    # Запускаем главный цикл обработки событий
    window.mainloop()

# Функция для обработки ввода попарных сравнений
def num2(window, criter):
    # Создаем и размещаем на окне текстовые поля для ввода попарных сравнений
    comparison_labels = []
    comparison_entries = []
    for i in range(criter):
        for j in range(criter):
            if i != j:
                label_text = "Сравните критерий {} с критерием {}: ".format(i+1, j+1)
                label = Label(window, text=label_text)
                label.pack()
                entry = Entry(window)
                entry.pack()
                comparison_labels.append(label)
                comparison_entries.append(entry)

    # Создаем и размещаем на окне кнопку для подтверждения ввода попарных сравнений
    knopka = Button(window, text="Подтвердить", command=lambda: num3(window, comparison_entries))
    knopka.pack()

# Функция для расчета весовых коэффициентов
def num3(window, entries):
    # Создаем список из введенных попарных сравнений
    comparisons = [float(entry.get()) for entry in entries]

    # Вычисляем сумму всех попарных сравнений
    suma = sum(comparisons)

    # Вычисляем весовые коэффициенты, нормируя значения попарных сравнений
    weights = [comparison / suma for comparison in comparisons]

    # Создаем и размещаем на окне текстовые поля для вывода весовых коэффициентов
    weights_labels = []
    for i, weight in enumerate(weights):
        label_text = "Весовой коэффициент для критерия {}: {:.2f}".format(i+1, weight)
        label = Label(window, text=label_text)
        label.pack()
        weights_labels.append(label)
# Вызываем функцию для создания графического интерфейса
num1()

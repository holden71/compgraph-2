from tkinter import Tk, PhotoImage, Canvas, NW
from PIL import Image

#В программе используется датасет DS2


def image_building(set_name, image_name, mode, image_size = (960,540)):
    image_size = image_size[::-1] if format == 1 else image_size 
    new_image = Image.new("RGB", image_size, "white") #создание картинки с заданным размером, фоном, цветовой палитрой
    f = open(set_name,"r") #открытие датасета
    splitted_data = f.read().split("\n")#разделение данных по строкам
    for i in range(len(splitted_data)-1): #рисуем пиксели
        splitted_data[i] = splitted_data[i].split(" ")
        if mode == 1:
            new_image.putpixel((int(splitted_data[i][0]), int(splitted_data[i][1])), (0, 0, 0))
        else:
            new_image.putpixel((int(splitted_data[i][1]), 540 - int(splitted_data[i][0]) if format == 3 else int(splitted_data[i][0])), (0, 0, 0))
    new_image.save(f"{image_name}.png")#сохранение картинки
    return image_size





def main_menu():

    dataset_name = input("Введите название датасета. (Пример: dataset.txt)\n> ")
    image_name = input("Введите название нового изображения:\n> ")
    mode_list = ("\nВыберите режим обработки (1 | 2 | 3):\n1. Прямое отображение (Не менять х и у)\n" #Выбор режима работы
                        "2. Обратное отображение (Поменять x и y местами)\n"
                        "3. Обратное отображение с нормальным отображением\n> ")
   
    mode = (int(input(mode_list)))
    while mode not in (1, 2, 3):
        mode = (int(input(mode_list)))

    size = image_building(dataset_name, image_name, mode) #создание картинки и возврат размера
    show_image = input("Хотите просмотреть фотографию? {Y/N}:\n") #просмотр результата

    if show_image.lower() == "y": #Отображение созданной картинки
        windowMain = Tk()
        windowMain.geometry(f'{size[0]}x{size[1]}+50+50')
        ph_im = PhotoImage(file=f'{image_name}.png')
        canv = Canvas(windowMain, width=size[0], height=size[1])
        canv.create_image(1, 1, anchor=NW, image=ph_im)
        canv.place(x=10, y=10)
        windowMain.mainloop()


    do_again = input("Хотите продолжить тестирование? {Y/N}:\n")
    if do_again.lower() == "y":
        main_menu()

main_menu()

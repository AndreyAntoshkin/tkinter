# Визуализация приложения с расписанием четная/нечетная недели
# Запуск через миниконду
from tkinter import *
import customtkinter                                        # pip3 install customtkinter
from PIL import Image, ImageTk                              # pip install pillow

def change_appearance_mode(new_appearance_mode):
    customtkinter.set_appearance_mode(new_appearance_mode)

def set_timetable():
    global main_frame_timetable
    global main_frame_homework
    global main_frame_settings
    
    switch_theme.place_forget()
    choose_week_box.place_forget()
    logo.place_forget()
    choose_days_box.place_forget()
    main_frame_timetable.grid_forget()
    main_frame_homework.grid_forget()
    main_frame_settings.grid_forget()
    button_timetable_generate.place(relx=0.9, rely=0.5, anchor=customtkinter.CENTER)
    choose_days_box.place(relx=0.35, rely=0.5, anchor=customtkinter.CENTER)
    choose_week_box.place(relx=0.65, rely=0.5, anchor=customtkinter.CENTER)
    logo.place(relx=0.08, rely=0.5, anchor=customtkinter.CENTER)

    main_frame_timetable.grid(row=1, column=0, padx=10, pady=10)
    main_frame_timetable.grid_columnconfigure(0, weight=1)

def set_homework():                                                                            # Функция создания заданий
    global main_frame_timetable
    global main_frame_homework
    global main_frame_settings
    
    switch_theme.place_forget()
    choose_week_box.place_forget()
    choose_days_box.place_forget()
    button_timetable_generate.place_forget()
    logo.place_forget()
    main_frame_timetable.grid_forget()
    main_frame_homework.grid_forget()
    main_frame_settings.grid_forget()
    logo.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    main_frame_homework.grid(row=1, column=0, padx=10, pady=10)
    main_frame_homework.grid_columnconfigure(0, weight=1)

    f = open("homework.txt")
    x = 0.1
    y = 0.15
    subst = ""
    mainst = f.readline()
    while mainst:
        subst = mainst.split(";", 1)[0]
        homework = customtkinter.CTkLabel(master=main_frame_homework, text=subst, fg_color=None, width=30, text_font=("Roboto Medium", 12))
        homework.place(relx=x, rely=y, anchor=customtkinter.CENTER)
        x = 0.6
        subst = mainst.split(";", 2)[1]
        homework = customtkinter.CTkLabel(master=main_frame_homework, text=subst, fg_color=None, width=100, text_font=("Roboto Medium", 14))
        homework.place(relx=x, rely=y, anchor=customtkinter.CENTER)
        x = 0.6
        y = y + 0.05
        subst = mainst.split(";", 3)[2]
        homework = customtkinter.CTkLabel(master=main_frame_homework, text=subst, fg_color=None, width=150, text_font=("Roboto Medium", 8))
        homework.place(relx=x, rely=y, anchor=customtkinter.CENTER)
        x = 0.1
        y += 0.15
        mainst = f.readline()
    f.close()

def set_settings():
    global main_frame_timetable
    global main_frame_homework
    global main_frame_settings
    
    switch_theme.place_forget()
    choose_week_box.place_forget()
    choose_days_box.place_forget()
    button_timetable_generate.place_forget()
    logo.place_forget()
    main_frame_timetable.grid_forget()
    main_frame_homework.grid_forget()
    main_frame_settings.grid_forget()

    main_frame_settings.grid(row=1, column=0, padx=10, pady=10)
    main_frame_settings.grid_columnconfigure(0, weight=1)

    switch_theme.place(relx=0.5, rely=0.05, anchor=customtkinter.CENTER)
    logo.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

def timetable_generate():                                                                            # Функция создания расписания
    global lesson
    global main_frame_timetable

    main_frame_timetable.destroy()
    main_frame_timetable = customtkinter.CTkFrame(master=window, corner_radius=15, height=680, width=450)
    main_frame_timetable.grid(row=1, column=0, padx=10, pady=10)
    main_frame_timetable.grid_columnconfigure(0, weight=1)

    f = open("lessons.txt")
    x = 0.1
    y = 0.2
    subst = ""
    mainst = f.readline()
    while mainst:
        subst = mainst.split(";", 1)[0]
        if choose_days_box.get() == subst:
            subst = mainst.split(";", 2)[1]
            if choose_week_box.get() == subst:
                subst = mainst.split(";", 3)[2]
                lesson = customtkinter.CTkLabel(master=main_frame_timetable, text=subst, fg_color=None, width=120, text_font=("Roboto Medium", 16))
                lesson.place(relx=x, rely=y, anchor=customtkinter.CENTER)
                x = 0.5
                subst = mainst.split(";", 4)[3]
                lesson = customtkinter.CTkLabel(master=main_frame_timetable, text=subst, fg_color=None, width=100, text_font=("Roboto Medium", 12))
                lesson.place(relx=x, rely=y, anchor=customtkinter.CENTER)
                x = 0.9
                subst = mainst.split(";", 5)[4]
                lesson = customtkinter.CTkLabel(master=main_frame_timetable, text=subst, fg_color=None, width=50, text_font=("Roboto Medium", 8))
                lesson.place(relx=x, rely=y, anchor=customtkinter.CENTER)
                x = 0.1
                y += 0.2
        mainst = f.readline()
    f.close()

# Установка темы
customtkinter.set_appearance_mode("System")  # Тема фона
customtkinter.set_default_color_theme("blue")  # Тема кнопок

window = customtkinter.CTk()

window.title('Расписание')                                  # Название окна
window.wm_attributes('-alpha', 0.96)                        # Прозрачность окна
window.geometry('480x800')                                  # Размер экрана
window.resizable(width=False, height=False)                 # Отключение возможности изменения размеров экрана

days = ("Выберите день","Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
weeks = ("Выберите неделю","Нечетная", "Четная")


# Блок Фреймов
top_frame = customtkinter.CTkFrame(master=window, corner_radius=0, height=50, width=480)
main_frame_timetable = customtkinter.CTkFrame(master=window, corner_radius=15, height=680, width=450) 
main_frame_homework = customtkinter.CTkFrame(master=window, corner_radius=15, height=680, width=450)
main_frame_settings = customtkinter.CTkFrame(master=window, corner_radius=15, height=680, width=450)
bot_frame = customtkinter.CTkFrame(master=window, corner_radius=0, height=50, width=480)

# Блок Кнопок
settings_image = ImageTk.PhotoImage(Image.open("settings.png").resize((20, 20))) #открытие картинок м присвоение их к переменной
photo = ImageTk.PhotoImage(Image.open("icons.png").resize((40,40)))                              # создал переменную фото присвоил ей картинку и ее размер
add_list_image = ImageTk.PhotoImage(Image.open("add-list.png").resize((20, 20)))
add_folder_image = ImageTk.PhotoImage(Image.open("add-folder.png").resize((20, 20)))
edit_image = ImageTk.PhotoImage(Image.open("edit.png").resize((20, 20)))

button_timetable = customtkinter.CTkButton(master=bot_frame, image=add_folder_image, text="Расписание", width=160,  height=50,
                                            corner_radius=8, fg_color=None, command=set_timetable)                                             #Кнопка меню расписание
button_homework = customtkinter.CTkButton(master=bot_frame, image=add_list_image, text="Задания", width=160,  height=50,
                                            corner_radius=8, fg_color=None, command=set_homework)                                             #Кнопка меню задания
button_settings = customtkinter.CTkButton(master=bot_frame, image=settings_image, text="Настройки", width=160, height=50,
                                            corner_radius=8, fg_color=None, command=set_settings)                                             #Кнопка меню настройки
switch_theme = customtkinter.CTkOptionMenu(master=main_frame_settings,values=["Dark", "Light", "System"]
                                            , command=change_appearance_mode)                                                       #Кнопка смены темы с вызовом функции
choose_week_box = customtkinter.CTkComboBox(master=top_frame, values=weeks)         
                               
choose_days_box = customtkinter.CTkComboBox(master=top_frame, values=days)                                                              #Вместо текста вставить картинку карандаша

button_timetable_generate = customtkinter.CTkButton(master=top_frame, text="Расписание", width=10,  height=40,
                                            corner_radius=8, text_font=("Roboto Medium", 8), command= timetable_generate)                       #Кнопка создания расписания

logo = customtkinter.CTkLabel(master=top_frame, text="SmartDesk", fg_color=None, width=60, text_font=("Roboto Medium", -10))        #Текст-логотип
window.iconphoto(False, photo)

def main():
    top_frame.grid(row=0, column=0) #расположение top frame разбиение на ячейки row строка column стообец (выбор дня, недели, кнопка расписание, название Smart Desk)
    top_frame.grid_columnconfigure(0, weight=1) 

    main_frame_timetable.grid(row=1, column=0, padx=10, pady=10) #расположение main frame 
    main_frame_timetable.grid_columnconfigure(0, weight=1) #само место

    bot_frame.grid(row=2, column=0) #расположение bot frame  нижняя часть
    bot_frame.grid_columnconfigure(0, weight=1) #параметры самой ячейки

    button_timetable.grid(row=0, column=0, padx=0, pady=0) 

    button_homework.grid(row=0, column=1, padx=0, pady=0)

    button_settings.grid(row=0, column=2, padx=0, pady=0)

    choose_week_box.place(relx=0.65, rely=0.5, anchor=customtkinter.CENTER) #располож в пикселях anchor опр часть виджета для котор задаются координаты

    choose_days_box.place(relx=0.35, rely=0.5, anchor=customtkinter.CENTER)

    logo.place(relx=0.08, rely=0.5, anchor=customtkinter.CENTER)

    button_timetable_generate.place(relx=0.9, rely=0.5, anchor=customtkinter.CENTER)

main()
window.mainloop()                                           # Открытие окна (Запуск постоянного цикла)
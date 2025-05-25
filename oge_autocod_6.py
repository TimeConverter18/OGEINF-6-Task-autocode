import flet as ft
from flet.core.canvas.color import Color
from flet.core.textfield import NumbersOnlyInputFilter


def task_6(data: str, log_ex: str, log_res: int, n: int, r: int):
    data = data.replace("–", "-").strip().replace(".","").split("; ")
    data = [eval(s) for s in data]

    log_ex = log_ex.replace("А", "a").replace("A", "a")
    f = lambda s, t, a: eval(log_ex)
    log_res = bool(log_res)
    if r!=2:
        r = range(1000, -1000, 1) if r else range(-1000, 1000, 1)

        for a in r:
            c = 0
            for e in data:
                s, t = e
                if f(s, t, a) == log_res:
                    c += 1
            if c == n: return a
    else:
        r = range(-1000, 1000, 1)
        k=0
        for a in r:
            c = 0
            for e in data:
                s, t = e
                if f(s, t, a) == log_res:
                    c += 1
            if c == n: k+=1
        return k


def main(page: ft.Page):
    def solve(e):
        if data_field.value and log_ex_field.value and n_field.value:
            log_res = 1 if log_res_field.value =="YES" else 0
            n = int(n_field.value)
            if r_field.value != "Кол-во значений параметра A":
                r = 0 if r_field.value == "Мин значение параметра A" else 1
            else:
                r=2
            solved_text.value = f"Ответ: {task_6(data_field.value, log_ex_field.value, log_res, n, r)}"
            page.update()

    page.fonts = {"gothic":"fonts/NewLetterGothicC.otf", "bold":"fonts/NewLetterGothicC-Bold.otf"}
    page.title = "Информатика ОГЭ АВТОКОД"

    page.window.width = 400
    page.window.height = 430
    page.window.min_width = 400
    page.window.min_height = 430
    page.window.max_width = 600
    page.window.max_height = 430

    page.theme = ft.Theme("gothic")
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    page.update()

    data_field = ft.TextField(label="Пары чисел в скобках")
    log_ex_field = ft.TextField(label="Условие, например (s > А) or (t > 11)")
    log_res_field = ft.Dropdown(label="Программа напечатает...", options=[ft.DropdownOption(text="YES"),ft.DropdownOption(text="NO")], width=180, value="YES", expand=True)
    n_field = ft.TextField(input_filter=NumbersOnlyInputFilter(), label="Сколько раз", width=120, expand=True)
    r_field = ft.Dropdown(options=[ft.DropdownOption(text="Мин значение параметра A"),ft.DropdownOption(text="Макс значение параметра A"), ft.DropdownOption(text="Кол-во значений параметра A")], width=300, value="Мин значение параметра A")
    solve_button = ft.Button(text="Решить", on_click=solve)
    solved_text = ft.Text(value="Ответ: ", size=18, font_family="bold")

    page.add(ft.Row([ft.Text("Введите параметры:", text_align=ft.TextAlign.CENTER, size=40, font_family="bold")], alignment=ft.MainAxisAlignment.CENTER),
             data_field,
             log_ex_field,
             ft.Row([log_res_field, n_field], alignment=ft.MainAxisAlignment.CENTER),
             ft.Row([ft.Text("Что нужно найти?")], alignment=ft.MainAxisAlignment.CENTER),
             ft.Row([r_field], alignment=ft.MainAxisAlignment.CENTER),
             ft.Row([solve_button, solved_text], alignment=ft.MainAxisAlignment.CENTER),
             )

page = ft.app(target=main, assets_dir="assets")
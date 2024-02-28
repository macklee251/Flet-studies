import flet as ft

def main(page: ft.Page):
    ad1 = ft.AlertDialog(
        title=ft.Text(value="Alert"),
        content=ft.Text(value="Hello, World!"),
        content_padding=ft.padding.all(30),                # Padding
        inset_padding=ft.padding.all(30),                  # Margin 
        modal = False,                                     # If you click outside the alert, it will close. Ele muda o ad1.open para False
        shape=ft.RoundedRectangleBorder(radius=5),
        on_dismiss=lambda _: print("fechei"),              # É uma função que é chamada quando o alerta é fechado
        actions=[
            ft.TextButton(text='Cancelar', style=ft.ButtonStyle(color=ft.colors.RED)),
            ft.ElevatedButton(text="Salvar", style=ft.ButtonStyle(bgcolor=ft.colors.GREEN, color=ft.colors.WHITE)),    
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )
    
    def open_ad(e):
        page.dialog = ad1
        ad1.open = True 
        page.update()
    
    
    btn1 = ft.ElevatedButton(text='Abrir', on_click=open_ad)
    
    page.add(btn1)
    
if __name__ == '__main__':
    ft.app(target=main)
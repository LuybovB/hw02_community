from datetime import datetime
current_datetime = datetime.now().date()
def year(request):
    """Добавляет переменную с текущим годом."""
    return {
        'year': int(current_datetime.strftime("%Y"))
    }

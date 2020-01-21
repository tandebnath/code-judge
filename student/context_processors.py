

def display_buttons(request):
    return {
        'display_buttons': request.session.has_key('logged_in')
    }


def student_details(request):
    if request.session.has_key('logged_in'):
        return{
            'student_details': dict(request.session)
        }
    else:
        return{
            'student_details': None
        }
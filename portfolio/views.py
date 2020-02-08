from django.shortcuts import render
from .models import PythonTutorial


# for the franklymade homepage
def franklymade_home(request):
    context = {}
    return render(request, 'sitetemplate/base.html', context)




# ******************************************
# for the python tutorials
def python_intro(request):
    
    context = {}
    return render(request, 'portfolio/python_intro.html', context)


def python_cours_details(request, course_id):
    
    course = PythonTutorial.objects.get(pk=course_id)
    

    if course.id == 1:
        context = {'course':course}
        return render(request, 'portfolio/variable_and_datatype.html', context)
    elif course_id == 2:
        context = {'course':course}
        return render(request, 'portfolio/operators_and_input.html', context)
    elif course_id == 3:
        context = {'course':course}
        return render(request, 'portfolio/conditions.html', context)
    elif course_id == 4:
        context = {'course':course}
        return render(request, 'portfolio/if_else.html', context)
    elif course_id == 5:
        context = {'course':course}
        return render(request, 'portfolio/nested_statements.html', context)
    elif course_id == 6:
        context = {'course':course}
        return render(request, 'portfolio/forloops.html', context)
    elif course_id == 7:
        context = {'course':course}
        return render(request, 'portfolio/whileloops.html', context)
    elif course_id == 8:
        context = {'course':course}
        return render(request, 'portfolio/listandtuple.html', context)
    elif course_id == 9:
        context = {'course':course}
        return render(request, 'portfolio/string_method.html', context)
    elif course_id == 10:
        context = {'course':course}
        return render(request, 'portfolio/string_method.html', context)
    elif course_id == 11:
        context = {'course':course}
        return render(request, 'portfolio/slice_operator.html', context)
    elif course_id == 12:
        context = {'course':course}
        return render(request, 'portfolio/functions.html', context)
    elif course_id == 13:
        context = {'course':course}
        return render(request, 'portfolio/reading_files.html', context)
    elif course_id == 14:
        context = {'course':course}
        return render(request, 'portfolio/writing_files.html', context)
    elif course_id == 15:
        context = {'course':course}
        return render(request, 'portfolio/listmethod.html', context)
    elif course_id == 16:
        context = {'course':course}
        return render(request, 'portfolio/modular_programing.html', context)
    elif course_id == 17:
        context = {'course':course}
        return render(request, 'portfolio/error_handling.html', context)
    elif course_id == 18:
        context = {'course':course}
        return render(request, 'portfolio/global_vs_loacal.html', context)
    elif course_id == 19:
        context = {'course':course}
        return render(request, 'portfolio/classes_and_objects.html', context)
    else:
        return render(request, 'portfolio/python_intro.html', context)
        









    

# def viewPortfolio(request):
    
#     context = {'projects':projects}
#     return render(request, 'portfolio/listandtuple.html', context)



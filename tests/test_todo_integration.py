from lib.todo import Todo
from lib.todo_list import TodoList

new_todo = Todo('TestTask1')

def test_todo_init():
    assert new_todo.task == 'TestTask1'
    assert new_todo.complete == False

def test_mark_complete():
    new_todo.mark_complete()
    assert new_todo.complete == True
from lib.todo import Todo
from lib.todo_list import TodoList

new_todo_incomplete = Todo('TestTask1')
new_todo_complete = Todo('TestTask2')
new_todo_complete.mark_complete()
new_todo_list = TodoList()
new_todo_list.add(new_todo_incomplete)
new_todo_list.add(new_todo_complete)

def test_todo_init():
    assert new_todo_incomplete.task == 'TestTask1'
    assert new_todo_incomplete.complete == False

def test_mark_complete():
    assert new_todo_complete.complete == True

def test_add():
    result = new_todo_list.contents
    assert result == [new_todo_incomplete, new_todo_complete]

def test_incomplete():
    result = new_todo_list.incomplete()
    assert result == [new_todo_incomplete]

def test_complete():
    result = new_todo_list.complete()
    assert result == [new_todo_complete]

def test_give_up():
    new_todo_list.give_up()
    result_incomplete = new_todo_list.incomplete()
    result_complete = new_todo_list.complete()    
    assert result_incomplete == []
    assert result_complete == [new_todo_incomplete, new_todo_complete]
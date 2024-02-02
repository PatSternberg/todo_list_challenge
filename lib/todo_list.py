class TodoList:
    def __init__(self):
        self.contents = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.contents.append(todo)

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        incomplete_list = []
        for entry in self.contents:
            if entry.complete == False:
                incomplete_list.append(entry)
        return incomplete_list

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        complete_list = []
        for entry in self.contents:
            if entry.complete == True:
                complete_list.append(entry)
        return complete_list        

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for entry in self.contents:
            entry.complete = True
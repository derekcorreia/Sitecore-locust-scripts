from locust import HttpLocust, TaskSet, task


class BasicTaskSet(TaskSet):

    @task(2)
    def root(self):
        self.client.get('/')

    @task(1)
    def about(self):
    	self.client.get('/en/About-Habitat/Introduction')

    @task(1)
    def projectmodules(self):
    	self.client.get('/en/Modules/Project')




class BasicTasks(HttpLocust):
    task_set = BasicTaskSet
    min_wait = 5000
    max_wait = 10000
    
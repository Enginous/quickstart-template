from HelloModel import HelloModel

class HelloController(object):
    @staticmethod
    def Test(data):
        # output "Name is John Appleseed" back through API
        return "My name is %s" % HelloModel.Name(data.name)
1class Call(object):
    def __init__(self, unique_id, name, phone_number, call_time, call_reason):
        self.unique_id = unique_id
        self.name = name
        self.phone_number = phone_number
        self.call_time = call_time
        self.call_reason = call_reason
    def displayInfo(self):
        print (self.unique_id, self.name, self.phone_number, self.call_time, self.call_reason)
class CallCenter(object):
    def __init__(self):
        super(Call, self).__init__(self, call_list, queue_size)
        self.call_list = call_list
        call_list = []
        self.call = [self.unique_id, self.name, self.phone_number, self.call_time, self.call_reason]
        self.queue_size = len(call_list)
    def add_call(self, call):
        self.call_list.append(call)
        return self
    def remove_call(self,call):
        self.call_list.remove(call_list[0])
        return self
    def info(self):
        print (queue_size)
CallFromTyler = Call(22,"Tyler","301-555-5555",0400,"to return a missed call")
CallCenter()

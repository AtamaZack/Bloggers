comments = []
class Comment:
    def __init__(self,comment_id,comment_title,comment_body,createdby):
        self.comment_id = comment_id
        self.comment_title = comment_title
        self.comment_body = comment_body
        self.createdby = createdby

    def create_comment(self):
        return {
            "comment_id": self.comment_id,
            "comment_title": self.comment_title,
            "comment_body": self.comment_body,
            "createdby": self.createdby,
            }

    def delete_comment(self, comment_id):
        if len(comments) > 0:
            try:
                returned_comment = [comment for comment in comments if comment["comment_id"] == int(comment_id)]
                comments.remove(returned_comment[0])
                return comments
            except Exception as error:
                return error   
        return False

    def edit_comment(self):
        pass
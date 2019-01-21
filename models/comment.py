class Comments:
    def __init__(self,comment_id,comment_title,comment_body,createdby):
        self.comment_id = comment_id
        self.comment_title = comment_title
        self.comment_body = comment_body
        self.createdby = createdby
        self.all_comments= []

    def get_comment(self):
        return {
            "comment_id": self.comment_id,
            "comment_title": self.comment_title,
            "comment_body": self.comment_body,
            "createdby": self.createdby,
            }

    def delete_comment(self, comment_id):
        if len(self.all_comments) > 0:
            try:
                returned_comment = [comment for comment in self.all_comments if comment["comment_id"] == int(comment_id)]
                self.all_comments.remove(returned_comment[0])
                return self.all_comments
            except Exception as error:
                return error   
        return False

    def edit_comment(self, comment_id,comment_title,comment_body,createdby ):
        returned_comment = [comment for comment in self.all_comments if comment["comment_id"] == int(comment_id)]
        returned_comment[0]['comment_title'] = comment_title
        returned_comment[0]['comment_body'] = comment_body
        returned_comment[0]['createdby'] = createdby
        return True


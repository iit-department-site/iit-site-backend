from src.wall.models import Post


class Feed:
        
    def get_post_list(self, user): 
        return  Post.objects.filter(user__owner__subscriber=user).order_by('-create_date').select_related('user').prefetch_related('comments')
    def get_single_post(self, pk): 
        return  Post.objects.get(id=pk).prefetch_related('comments')
            
            
feed_service = Feed()
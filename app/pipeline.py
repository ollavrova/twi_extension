from app.models import Followers
from twi_extension.settings import SOCIAL_AUTH_TWITTER_KEY, SOCIAL_AUTH_TWITTER_SECRET, access_token_key, access_token_secret
import twitter


def update_followers(backend, user, response, *args, **kwargs):
    if backend.name == 'twitter':
        api = twitter.Api(consumer_key=SOCIAL_AUTH_TWITTER_KEY,
                          consumer_secret=SOCIAL_AUTH_TWITTER_SECRET,
                          access_token_key=access_token_key,
                          access_token_secret=access_token_secret)
        followers = api.GetFollowers(include_user_entities=True, screen_name=response.get('screen_name'))
        for f in followers:
            ff, _ = Followers.objects.get_or_create(user=user, id_str=f.id, screen_name=f.screen_name)
            ff.created_at = f.created_at
            ff.url = f.url
            ff.location = f.location
            ff.description = f.description
            ff.save()

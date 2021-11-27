from constants.prompt_selections import MC


class MC(object):
    # Prompt Selections
    PG = MC.PG.value.upper() if MC.PG.value else 'ALL SHOPPERS'
    COMP_PG = MC.COMP_PG.value.upper() if MC.COMP_PG.value else 'ALL SHOPPERS'
    # Media Consumption Tab Headers
    MC_HEAD = ['{}', '% ' + PG, '% ' + COMP_PG, 'INDEX']
    # Summary Headers & Tables
    SUMMARY_HEAD = ['TECHNOLOGY ADOPTION', 'PC USAGE', 'MOBILE USAGE', 'TV USAGE', 'MOBILE APP BEHAVIOR',
                    'ONLINE BEHAVIOR', 'TELEVISION BEHAVIOR', 'ONLINE / OFFLINE BEHAVIOR']
    SUMMARY_TABLE = [
        # Technology Adoption
        'Laggards', 'Late Majority', 'Early Majority', 'Early Adopters', 'Innovators',
        # PC Usage
        'More than 8 hours per day', '6-8 hours per day', '3-5 hours per day',
        '1-2 hours per day', 'Less than 1 hour per day', 'I do not access a PC daily',
        # Mobile Usage
        'More than 8 hours per day', '6-8 hours per day', '3-5 hours per day',
        '1-2 hours per day', 'Less than 1 hour per day', 'I do not use daily',
        # TV Usage
        'More than 8 hours per day', '6-8 hours per day', '3-5 hours per day',
        '1-2 hours per day', 'Less than 1 hour per day', 'I do not watch TV daily',
        # Mobile App Behavior
        'Banking', 'Books', 'Dating', 'Entertainment (videos / shows)', 'Food + Drink', 'Games',
        'Health + Fitness', 'Kids / Parenting', 'Lifestyle', 'Magazines / Newspapers',
        'Maps / Navigation', 'Messaging / Chat', 'Music / Audio', 'News', 'Restaurant', 'Shopping',
        'Social Media', 'Sports', 'Travel', 'Weather', 'None of the above',
        # Online Behavior
        'Played games', 'Made shopping list', 'Researched products',
        'Made an online purchase', 'Listened to music / radio', 'Watched videos / shows',
        'Ordered food for delivery', 'Researched recipes', 'Interacted w/Smart Home device',
        'Visited social media platform', 'None of the above',
        # Television Behavior
        'Watched live programming', 'Watched time-shifted content', 'Watched a Blu-ray or DVD',
        'Played video games', 'Bought / rented content online', 'Streamed free content',
        'Streamed subscription service', 'None of the above',
        # Online / Offline Behavior
        'Listen to AM/FM Radio', 'Listen to Podcasts', 'Read Newspaper (Print)',
        'Read Newspaper (Digital)', 'None of the above']
    # Watching Headers & Tables
    WATCH_HEAD = ['DEVICE OWNERSHIP, HOME ENTERTAINMENT', 'STREAMING VIDEO']
    WATCH_TABLE = [
        # Device Ownership, Home Entertainment
        'Smart TV', 'Blu-Ray / DVD Player', 'Digital Video Recorder (DVR)', 'Cable Box',
        'Satellite Box', 'Microsoft XBOX', 'Nintendo', 'Sony PlayStation', 'Amazon Fire TV',
        'Apple TV', 'Google Chromecast', 'Sling TV', 'None of the above',
        # Streaming Video
        'Amazon Video (Prime)', 'CBS All Access', 'DirecTV Now', 'HBO GO / HBO NOW', 'Hulu',
        'MLB.TV', 'Netflix', 'Showtime Anytime', 'STARZ Play', 'YouTube Red', 'YouTube TV', 'None of the above']
    # Listening Headers & Tables
    LISTEN_HEAD = ['STREAMING']
    LISTEN_TABLE = [
        # Streaming
        'Amazon Music (Prime)', 'Apple Music / iTunes', 'Google Play', 'iHeart Radio', 'NPR One',
        'Pandora', 'SiriusXM Radio', 'SoundCloud', 'Spotify', 'Tidal', 'TuneIn Radio', 'None of the above']
    # Reading Headers & Tables
    READ_HEAD = ['TOP 20 MAGAZINES', 'TOP 10 MAGAZINE TOPICS']
    READ_TABLE = [
        # Top 20 Magazines
        'AARP', 'AAA Living', 'Better Homes and Gardens', 'Cosmopolitan', 'Costco Connection',
        'Family Circle', 'Game Informer', 'Glamour', 'Good Housekeeping', 'National Geographic',
        'O, The Oprah Magazine', 'Parents', 'People', "Reader's Digest", 'Shape', 'Southern Living',
        'Sports Illustrated', 'Taste of Home', 'Time', "Women's Day", 'None of the above',
        # Top 10 Magazine Topics
        'Entertainment', "Men's Style / Fashion", "Women's Style / Fashion", 'Sports',
        'News / Politics', 'Travel', 'Health + Fitness', 'Cooking / Food + Wine',
        'Home / Decor', 'Children / Teen', 'Other', 'None']
    # Social Media Headers & Tables
    SOCIAL_HEAD = ['SOCIAL MEDIA BEHAVIORS', 'SOCIAL MEDIA PLATFORMS', 'SOCIAL MEDIA USAGE']
    SOCIAL_TABLE = [
        # Social Media Behaviors
        'Share status updates', 'Post photos or videos', 'Keep in touch', 'Follow friends / family',
        'Make new friends', 'Professional networking', 'For product reviews / ratings',
        'For products / services', 'For news / current events', 'For movies / TV / music',
        'For local events', 'Support businesses / orgs', 'Exclusive offers', 'I do not use social media',
        # Social Media Platforms
        'Facebook', 'Twitter', 'Pinterest', 'Instagram', 'Snapchat', 'Tumblr',
        'Google Plus', 'LinkedIn', 'Reddit', 'None of the above',
        # Social Media Usage
        'Several times per day', 'Several times per week', 'Several times per month',
        'Once a month or less', 'I do not use social media']

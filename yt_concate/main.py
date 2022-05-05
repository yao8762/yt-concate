import sys
import getopt

from yt_concate.pipeline.steps.prelight import Preflight
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.initialize_yt import InitializeYT
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.pipeline.steps.read_caption import ReadCaption
from yt_concate.pipeline.steps.search import Search
from yt_concate.pipeline.steps.download_videos import DownloadVideos
from yt_concate.pipeline.steps.edit_video import EditVideo
from yt_concate.pipeline.steps.postlight import Postflight
from yt_concate.pipeline.steps.step import StepException
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.utils import Utils


CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'
short_opts = 'hc:s:l:'
long_opts = 'help channel_id= search_word= limit='.split()


def print_usage():
    print('python test2.py OPTIONS')
    print('OPTIONS:')
    print('{:>6} {:<20}{}'.format('-c', '--channel_id', 'channel id of the Youtube channel to download'))
    print('{:>6} {:<20}{}'.format('w', '--search_word', 'Search words from subtitles on Youtube channel'))
    print('{:>6} {:<20}{}'.format('l', '--limit', 'Maximum number of clips for merged videos'))


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'incredible',
        'limit': 20,
    }

    try:
        opts, args = getopt.getopt(sys.argv[1:], short_opts, long_opts)
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == ("-h", "--help"):
            print_usage()
            sys.exit(0)
        elif opt in ("-c", "--channel_id"):
            inputs['channel_id'] = arg
        elif opt in ("-s", "--search_word"):
            inputs['search_word'] = arg
        elif opt in ("-l", "--limit"):
            inputs['limit'] = int(arg)

    if inputs['channel_id'] == "" or inputs['search_word'] == "":
        print_usage()
        sys.exit(2)

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        DownloadVideos(),
        EditVideo(),
        Postflight(),
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()

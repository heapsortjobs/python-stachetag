__author__ = 'ckinsey'

import re


class StacheTag(object):
    """
    Represents a parsed StacheTag
    """

    def __init__(self, stachetag, *args, **kwargs):
        """
        Takes a textual stachetag and turns it into a bonafide StacheTag
        """

        # Ensure the authenticity of the stachetag
        if not re.match(r'^\S+\{$', stachetag):
            raise ValueError("Stachetag %s does not smell like a stachetag." % stachetag)

        self.tag = stachetag[:-1]
        self.stachetag = stachetag


class StacheWaxer(object):
    """
    Takes a string, and can format its stachetags or return lists of stachetags
    """

    def __init__(self, string, *args, **kwargs):
        self._original_string = string
        self._stache_cache = None

    def __iter__(self):
        """
        OMG ITS ITERABLE
        """
        for stache in self.cached_staches():
            yield stache

    def get_tags(self):
        """
        Gets boring old tags in word format.
        """

        return [stache.tag for stache in self.cached_staches()]

    def get_stachetags(self):
        """
        Gets awesome tags in stachetag format
        """
        return [stache.stachetag for stache in self.cached_staches()]

    def get_hashtags(self):
        """
        Gets stachtag in antiquated hashtag format
        """
        raise NotImplementedError("Ain't gonna happen baby!")

    def cached_staches(self):
        """
        Finds all staches or returns the cache.  Makes stachetag parsing lazy
        """
        if self._stache_cache is None:
            self._stache_cache = [StacheTag(stache) for stache in re.findall(r'\S+\{', self._original_string)]

        return self._stache_cache

    def format_staches(self, format_string=None):
        """
        Takes a format string and uses it to format the original string

        i.e.:
        > waxer.format_staches(format_string="<a href='#{tag}'>{stachetag}</a>")
        "string with <a href='#awesome'>awesome{</a> stachetags!"

        """

        if format_string is None:
            raise ValueError('StacheStash.format_tags requires a format_string argument!')

        parsed_format_string = format_string.format(**{'tag': '\\1', 'stachetag': '\\1{'})

        return re.sub(r'(\S+)\{', parsed_format_string, self._original_string)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from modules.crawler import WCrawler


class MethodCrtSh:

    def __init__(self, context):

        # The main context
        self.context = context

        # Unique only
        self.hostnames = []


    def find(self, hostnameBase):

        # Use the crawler bot
        crawler = WCrawler()

        # json result
        result = None

        try:
            result = crawler.httpRequest(
                url='https://crt.sh/?q=' + crawler.urlencode('%.' + hostnameBase) + '&output=json'
            )

            # Free memory (no navigation context)
            crawler.clearContext()

        except Exception as e:
            self.context.out(
                self.context.strings['methods']['crt-sh']['no-connect']
            )
            return

        # The http response is success?
        if(result['status-code'] != 200):
            self.context.out(
                message=self.context.strings['methods']['crt-sh']['wrong-status-http'],
                parseDict={
                    'id': result['status-code']
                }
            )
            return

        try:
            # Convert the result into json object
            result = json.loads(result['response-content'])

        except Exception as e:
            self.context.out(
                self.context.strings['methods']['crt-sh']['corrupt-response']
            )
            return

        if(
            (not isinstance(result, list)) or
            (len(result) == 0)
        ):
            self.context.out(
                self.context.strings['methods']['crt-sh']['empty']
            )
            return

        # Process each hostname
        for item in result:

            # Drop root wildcards
            if(item['name_value'] == ('*.' + hostnameBase)):
                continue

            if(not item['name_value'] in self.hostnames):

                # For unique resulsts
                self.hostnames.append(item['name_value'])

                # Add full hostname
                self.context.addHostName(
                    hostname=item['name_value'],
                    messageFormat=self.context.strings['methods']['crt-sh']['item-found']
                )

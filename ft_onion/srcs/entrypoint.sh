#!/bin/sh
service tor start
exec nginx -g "daemon off;"

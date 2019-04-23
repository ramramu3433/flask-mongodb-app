#!/bin/sh

echo $$ > app.pid
exec "$@"

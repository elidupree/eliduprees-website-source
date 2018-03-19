#!/bin/bash
rsync -av --del --exclude "temp-hilariou*" /n/autobuild/eliduprees-web-games/build/static/media/web-games/ ./media/vendor/web-games
cp /n/autobuild/eliduprees-web-games/build/target/asmjs-unknown-emscripten/release/the_path.js ./media/vendor/
cp /n/autobuild/eliduprees-web-games/build/static/the_path.html ./vendor/

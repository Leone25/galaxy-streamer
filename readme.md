# Galaxy Streamer

Stream content from your browser to your [cosmic unicorn](https://shop.pimoroni.com/products/cosmic-unicorn).

## Why?

Because of rule 86 of the internet: if it has at least 2 states it can play bad apple.

## How?

I'm using [microWebSrv](https://github.com/jczic/MicroWebSrv) to host 2 simple static pages + a websocket, which is used to receive the video feed. The pages take care of capturing the video (either from the user screen or from a video file), scaling it down, extracting the image data (and flipping the bytes around since js uses RGBA, but cosmic unicorn uses BGRA) and then it's just piped over to the pico which puts the data into it's frame buffer.

## Does it work?
[Yes, ofc.](https://www.tiktok.com/@leone2503/video/7214202304990432518)

## Downsides 
- Very unstable
- For whatever reason microWebSrv won't run if it's not on the main thread so if the user is connected to the websocket it won't load the page (to bypass this you have to close and reopen the page every time you want to refresh)
- A shit-ton of delay
- Video playback occasionally freezes on the pico, no idea, in part has to do with the browser grouping messages before sending them, use firefox to mostly avoid this problem

## How to use?
Upload all the files with this same folder structure to your pico and reset it. Then navigate to its ip on the network (it's showed in the serial output too), just select a video file and press start.
To use the screen grab you'll need a reverse proxy to run on https; you can use ngrok by running `ngrok http <ip-of-pico>:80` and then navigate to the ngrok url + `/screen.html`, press start and give permision to capture the screen.

## Could this be improved?
Absolutely, not by me tho, this is just a proof of concept, a personal challange and, most importantly, a meme.

## Credits
- [Pimoroni](http://pimoroni.com/) for the cosmic unicorn and for the awesome support
- [microWebSrv](https://github.com/jczic/MicroWebSrv)

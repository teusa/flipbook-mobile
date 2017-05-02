# flipbook-mobile

Scroll-based inline flipbook animation for mobile and desktop.


## Installation

``` npm install flipbook-mobile```

or 

``` <script src="flipbook.js"></script> ```



## Usage

``` html
<div id='walk-cycle'></div>

<script>
	flipbook({
		id: 'walk-cycle',
		filename: index => `https://<my_image_server>/my_flipbook_frames/${index}.jpg`,
		count: 86,
		speed: 0.5
	});
</script>
```

## Options
* **id** (required)
	[String] The id of the element where the flipbook will be inserted.

* **filename** (required)
	[Function] Given frame index, returns URL to frame image.

* **count** (required)
	[Number] Count of images in directory.

* **speed** (optional)
	[Number 0 to 1] How fast the scroll advances the frames (0: slow, 1: fast). Defaults to 0.5.

* **cover** (optional)
	[Boolean] If the flipbook should go full window height, and center-crop (like CSS's `background-size: cover`). Defaults to false.

* **loaded** (optional)
	[Function] Callback function when the flipbook has loaded all images and is ready to play through. Defaults to none.

* **gif** (optional)
	[Boolean] Autoplay the animation and loop like a gif without scroll interaction.


### Helpful bits
Convert a video to image sequence with ffmpeg:

```ffmpeg -i input.mp4 -r 12 frames/%d.png ```


## License & Credit
Original [flipbook.js](https://github.com/russellgoldenberg/flipbook.js):
> MIT © [Russell Goldenberg](http://russellgoldenberg.com)
>
> Inspired by [canvid](https://github.com/gka/canvid/blob/master/canvid.js) and [stack](https://github.com/mbostock/stack)

<script lang="ts">
  import type { Pair } from '$lib/types.ts';
  import { Card } from 'flowbite-svelte';
  import Element from '$lib/element.svelte';

  export let collisionCheck;
  export let pair: Pair;
  export let one_or_two: number;

  export let dom;

  function efunc(node) {
    let moving = false;
    // The lines below are for randomizing the starting points of the tiles
    // that are responsible for the matching game.
    let left = Math.random() * window.innerWidth;
    let top = Math.random() * window.innerHeight;

    // offset from upper left corner to mouse
    let offsetX;
    let offsetY;

    node.style.position = 'absolute';
    node.style.top = `${top}px`;
    node.style.left = `${left}px`;
    node.style.cursor = 'move';
    node.style.userSelect = 'none';

    // The following eventlistener is triggered when the mouse is pressed down
    // so when the tile is getting dragged the coordinates carry through
    node.addEventListener('mousedown', (e) => {
      moving = true;
      offsetX = e.clientX - left;
      offsetY = e.clientY - top;
    });

    // The following eventlistener follows the mouse coordinates and makes the tile follow it
    window.addEventListener('mousemove', (e) => {
      if (moving) {
        left = e.clientX - offsetX;
        top = e.clientY - offsetY;
        node.style.top = `${top}px`;
        node.style.left = `${left}px`;
      }
    });

    // The last eventlisterner is for when the mouse button is finally moved in which case the tile stops
    // moving with the mouse.
    window.addEventListener('mouseup', () => {
      moving = false;
      collisionCheck(node, pair);
    });
  }
</script>

<svelte:options accessors={true} />

<div use:efunc bind:this={dom}>
  <Card class="max-w-max">
    <Element {pair} {one_or_two} />
  </Card>
</div>

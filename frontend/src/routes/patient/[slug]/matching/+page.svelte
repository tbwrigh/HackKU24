<script lang='ts'>
  import type { PageData } from './$types';
  import type { Pair } from '$lib/types';
  import Draggable from '$lib/draggable.svelte';
  import ReturnModal from '$lib/returnModal.svelte';

  export let data: PageData;

  let won: bool = false;
  let draggables = []

  function collisionCheck(thisdom, thispair) {
    if (won) return;

    const rect1 = thisdom.getBoundingClientRect();

    draggables.forEach((otherDraggable) => {
      // can't collide with ourselves
      if (otherDraggable.dom === thisdom) return;

      const rect2 = otherDraggable.dom.getBoundingClientRect();

      if (
        rect2.right  > rect1.left   &&
        rect2.left   < rect1.right  &&
        rect2.top    < rect1.bottom &&
        rect2.bottom > rect1.top
      ) {
        thisdom.style.transition = 'opacity 1s';
        otherDraggable.dom.style.transition = 'opacity 1s';

        // correct match
        if (otherDraggable.pair.id == thispair.id) {
          thisdom.style.opacity = '0';
          otherDraggable.dom.style.opacity = '0';
          setTimeout(() => {
            thisdom.remove();
            otherDraggable.dom.remove();
            // if for every draggable, its dom is undefined or has been removed
            if (draggables.every((d) => d.dom === undefined || !d.dom.checkVisibility())) {
              won = true;
            }
          }, 1000);
        }

        // incorrect match
        else {
          thisdom.style.opacity = '1';
          otherDraggable.dom.style.opacity = '1';
          thisdom.style.backgroundColor = 'red';
          otherDraggable.dom.style.backgroundColor = 'red';

          // revert white background color back to red after a delay
          setTimeout(() => {
            thisdom.style.backgroundColor = 'white';
            otherDraggable.dom.style.backgroundColor = 'white';
          }, 1000);
        }

      }
    });
  }

</script>

{#each data.pairs as pair, i}
  <Draggable {pair} {collisionCheck} one_or_two={1} bind:this={draggables[2*i]} />
  <Draggable {pair} {collisionCheck} one_or_two={2} bind:this={draggables[2*i+1]} />
{:else}
  <p>No pairs detected for this patient</p>
{/each}

<ReturnModal open={won} route={"matching"} />

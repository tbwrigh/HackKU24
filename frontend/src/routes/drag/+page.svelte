<script lang="ts">
	import { Card } from 'flowbite-svelte';
	import { ElementType } from '$lib/types.ts';
	import Element from '$lib/element.svelte';
	

	function element(node) {
		let moving = false;
		// The lines below are for randomizing the starting points of the tiles
		// that are responsible for the matching game.
		let left = Math.random() * window.innerWidth;
		let top = Math.random() * window.innerHeight;
  
		node.style.position = 'absolute';
		node.style.top = `${top}px`;
		node.style.left = `${left}px`;
		node.style.cursor = 'move';
		node.style.userSelect = 'none';
  
		// The following eventlistener is triggered when the mouse is pressed down
		// so when the tile is getting dragged the coordinates carry through
		node.addEventListener('mousedown', () => {
			moving = true;
		});
  
		// The following eventlistener follows the mouse coordinates and makes the tile follow it
		window.addEventListener('mousemove', (e) => {
			if (moving) {
				left = e.clientX - 50;
				top = e.clientY - 15;
				node.style.top = `${top}px`;
				node.style.left = `${left}px`;
			}
		});
  
		// The last eventlisterner is for when the mouse button is finally moved in which case the tile stops
		// moving with the mouse.
		window.addEventListener('mouseup', () => {
			moving = false;
			const nodes = document.querySelectorAll('.element');
			nodes.forEach((otherNode) => {
				if (otherNode !== node) {
					/*
					const rect1 = node.getBoundingClientRect();
					const rect2 = otherNode.getBoundingClientRect();
					const buffer = 100;
					if (
						Math.abs(rect1.left - rect2.left) <= buffer &&
						Math.abs(rect1.top - rect2.top) <= buffer
					) {
						node.style.transition = 'opacity 1s';
						otherNode.style.transition = 'opacity 1s';
						node.style.opacity = '0';
						otherNode.style.opacity = '0';
						setTimeout(() => {
							node.remove();
							otherNode.remove();
						}, 1000);
						console.log('Overlap detected!');
						*/
						const rect1 = node.getBoundingClientRect();
					const rect2 = otherNode.getBoundingClientRect();
					const buffer = 100;
					// The following if statement is for carrying out the math behind "matching" the tiles
					// and making sure that they are overlapping.
					if (
						Math.abs(rect1.left - rect2.left) <= buffer &&
						Math.abs(rect1.top - rect2.top) <= buffer
					) {
						node.style.transition = 'opacity 1s';
						otherNode.style.transition = 'opacity 1s';
						node.style.opacity = '0';
						otherNode.style.opacity = '0';
						node.style.opacity = '1';
						otherNode.style.opacity = '1';						
						
							node.style.backgroundColor = "red";
							otherNodestyle.backgroundColor = "red";
						setTimeout(() => {
							node.style.backgroundColor = "white";
							otherNodestyle.backgroundColor = "white";
						}, 1000);
						
					}
				}
			});
		});
	}
  // Finally this last bit of code is for running the entire element four times in order to get four individual
  // tiles. This number can change later down the road depending on how many tiles the player wants to play 
  // with.	
  </script>
  {#each {length: 4} as _, i}
  <div use:element class="element">
	<Card class="w-fit">
	  <Element value={"hello!"} type={ElementType.Text}/>
	</Card>
  </div>
  {/each}
  

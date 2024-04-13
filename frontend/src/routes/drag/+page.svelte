<script lang="ts">
	import { Card } from 'flowbite-svelte';
	import { ElementType } from '$lib/types.ts';
	import Element from '$lib/element.svelte';
	
	function element(node) {
		let moving = false;
		let left = Math.random() * window.innerWidth;
		let top = Math.random() * window.innerHeight;
  
		node.style.position = 'absolute';
		node.style.top = `${top}px`;
		node.style.left = `${left}px`;
		node.style.cursor = 'move';
		node.style.userSelect = 'none';
  
		node.addEventListener('mousedown', () => {
			moving = true;
		});
  
		window.addEventListener('mousemove', (e) => {
			if (moving) {
				left = e.clientX - 50;
				top = e.clientY - 15;
				node.style.top = `${top}px`;
				node.style.left = `${left}px`;
			}
		});
  
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

  </script>
  
  {#each {length: 4} as _, i}
  <div use:element class="element">
	<Card class="w-fit">
	  <Element value={"hello!"} type={ElementType.Text}/>
	</Card>
  </div>
  {/each}
  
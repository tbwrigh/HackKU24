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
					 left = e.clientX-50;
					 top = e.clientY-15;
					 node.style.top = `${top}px`;
					 node.style.left = `${left}px`;
				}
		 });
		
		 window.addEventListener('mouseup', () => {
			 moving = false;
		 });
	
	}
</script>

{#each {length: 4} as _, i}
  <div use:element>
	<Card class="w-fit">
		<Element value={"hello!"} type={ElementType.Text}/>
	</Card>
  </div>
  {/each}


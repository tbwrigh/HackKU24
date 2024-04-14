<script lang="ts">
    import { onMount } from 'svelte';
    import { page } from '$app/stores';
    import type { SelectItem, Puzzle } from '$lib/types';

    import Selection from '$lib/selection.svelte';

    const backendUrl = import.meta.env.VITE_BACKEND_URL;

    let puzzles: SelectItem[] = [];

    onMount(async () => {
        console.log('Puzzles page mounted');

        const res = await fetch(`${backendUrl}/puzzle/patient/${$page.params.slug}`);

        if (res.ok) {
            const data: Puzzle[] = await res.json();
            data.forEach((puzzle: Puzzle) => {
                const item = { href: `/patient/${$page.params.slug}/puzzles/${puzzle.id}`, label: puzzle.name };
                puzzles = [...puzzles, item];
            });
        } else {
            console.error('Error:', res.statusText);
        }
    });


</script>

<Selection heading="Puzzles" options={puzzles} />
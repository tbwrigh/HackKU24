import type { PageLoad } from './$types';

const backendUrl = import.meta.env.VITE_BACKEND_URL;

export const load: PageLoad = async ({ fetch, params }) => {
  let json = undefined;
  try {
    const response = await fetch(`${backendUrl}/patient/${params.slug}`);
    json = await response.json();
  } catch (error) {
    console.error('Error:', error);
  }
  return {
    slug: json.id,
    name: json === undefined ? 'error' : json.name,
  };
};

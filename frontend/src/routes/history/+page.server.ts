import type { PageServerLoad } from "./$types";

export const load: PageServerLoad = async ({ url }) => {
	const href = url.href;
};
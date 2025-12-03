import rss from '@astrojs/rss';
import errorData from '../data/errors.json';
import layoffData from '../data/layoffs.json'; // Used for OBD2
import saasData from '../data/saas.json';
import llcData from '../data/llc.json';

export async function GET(context) {
    const siteId = import.meta.env.SITE_ID || 'errors';

    // 1. Select Data & Domain
    let data = errorData;
    let siteUrl = 'https://applianceerror.com';

    if (siteId === 'layoffs') {
        data = layoffData;
        siteUrl = 'https://errorcodehelp.com';
    } else if (siteId === 'saas') {
        data = saasData;
        siteUrl = 'https://saasguide.org';
    } else if (siteId === 'llc') {
        data = llcData;
        siteUrl = 'https://llcguide.org';
    }

    // 2. Generate Items (Limit to 50 most recent to avoid timeouts)
    const items = data.slice(0, 50).map((item) => {
        const slug = item.slug?.toString().toLowerCase().trim().replace(/\s+/g, '-') || 'home';
        const imageUrl = `${siteUrl}/social/${slug}.png`;

        return {
            title: item.title,
            description: item.content || `Guide for ${item.title}`,
            link: `${siteUrl}/${slug}`,
            pubDate: new Date(),
            // Pinterest specific image tag
            customData: `<media:content url="${imageUrl}" medium="image" />`,
        };
    });

    return rss({
        title: `${siteId.toUpperCase()} Updates`,
        description: `Latest guides from ${siteUrl}`,
        site: siteUrl,
        items: items,
        xmlns: {
            media: 'http://search.yahoo.com/mrss/',
        },
    });
}

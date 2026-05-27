# Manual Setup Required

## 1. Netlify GitHub OAuth

1. Go to Netlify Dashboard → Site Settings → Access Control → OAuth
2. Add GitHub OAuth provider
3. Callback URL: `https://api.netlify.com/auth/done`
4. Ensure editor has write access to `Doctor2kUa/alenam-art`

## 2. Cloudflare R2

1. Create R2 bucket
2. Set CORS policy:

```json
[
  {
    "AllowedHeaders": ["*"],
    "AllowedMethods": ["GET", "PUT", "HEAD"],
    "AllowedOrigins": ["https://alenam.art", "https://*.netlify.app"],
    "ExposeHeaders": ["ETag"],
    "MaxAgeSeconds": 3000
  }
]
```

3. In Sveltia CMS (`/admin/`), configure R2 media library:
   - Access Key ID: from R2 dashboard
   - Secret Access Key: entered via UI (NOT in repo)
   - Bucket name
   - Account ID
   - Public URL: `https://media.alenam.art`
   - Prefix: `uploads/`

## 3. Netlify Environment Variable

Set in Netlify Dashboard → Site Settings → Environment Variables:

```
PUBLIC_MEDIA_BASE_URL=https://media.alenam.art
```

## 4. After Merge to Main

1. Change `branch` in `public/admin/config.yml` from `feature/sveltia-cms-r2-migration` to `main`
2. Or enable Sveltia editorial workflow
3. Move images from `public/uploads/` to R2 bucket preserving `uploads/YYYY/MM/` structure

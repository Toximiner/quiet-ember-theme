const {getOIDCCredential}=require('@vscode/vsce/out/oidc');
const {getGalleryAPI}=require('@vscode/vsce/out/util');
(async()=>{
 const credential=await getOIDCCredential('Toximiner');
 const gallery=await getGalleryAPI(credential);
 await gallery.deleteExtension('Toximiner','quiet-ember-theme','1.0.0');
 console.log('Removed retired Marketplace version 1.0.0.');
})().catch(error=>{console.error(error.message);process.exitCode=1;});

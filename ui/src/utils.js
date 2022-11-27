export const openInNewWin = (url)=>{
    const fn = async () => {
        let res = await fetch(`http://127.0.0.1:8080/?url=${url}`);
    }
    fn();
}

import { useEffect } from "react";
import ResultMain from "../components/ResultMain";
import ResultMore from "../components/ResultMore";
import ResultRelated from "../components/ResultRelated"
import Styles from "../css/result.module.css"
import config from "../config"
// In the main process.



// Or load a local HTML file
// win.loadFile('index.html')
const ResultPage = () => {
    useEffect(() => {
        let url = "https://leetcode.com/problems/subarray-sum-equals-k/";
        const fn = async () => {
            let res = await fetch(`http://127.0.0.1:8080/?url=${url}`);
        }
        fn();
        fn();
    }, []);
    return ( <div></div>)
        // <div className={Styles.ResultContainer}>
        //     <div className={Styles.ResultMain}>
        //         <ResultMain />
        //     </div>
        //     <div className={Styles.ResultExtra}>
        //         <ResultMore/>
        //         <ResultRelated/>
        //     </div>
        // </div>
}

export default ResultPage;
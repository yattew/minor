
import { useEffect } from "react";
import ResultMore from "../components/ResultMore";
import ResultRelated from "../components/ResultRelated"
import Styles from "../css/result.module.css"
import config from "../config"
import { openInNewWin } from "../utils";

const ResultPage = () => {
    useEffect(() => {
        let url = "https://www.geeksforgeeks.org/maximum-sum-path-across-two-arrays/";
        // openInNewWin(url);
    }, []);
    return (
        <div className={Styles.ResultContainer}>
            <div className={Styles.ResultInfo}>
                <h3>your search result is being openend in a new window</h3>
            </div>
            <div className={Styles.ExtraContainer}>
                <ResultMore />
                <div className={Styles.Divider}></div>
                <ResultRelated />
            </div>
        </div>

    )
}

export default ResultPage;
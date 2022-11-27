
import { useEffect, useState } from "react";
import ResultMore from "../components/ResultMore";
import ResultRelated from "../components/ResultRelated"
import Styles from "../css/result.module.css"
import config from "../config"
import { openInNewWin } from "../utils";
import { useParams } from "react-router-dom";

const ResultPage = () => {
    const { item } = useParams();
    const [results, setResults] = useState([]);
    const [related, setRelated] = useState([]);
    const [more, setMore] = useState([]);
    useEffect(() => {
        console.log("from result page:", item);
        const fn = async () => {
            let query = item;
            let host_addr = config.host_addr;
            let res = await fetch(host_addr + "result/" + query);
            if (res.ok) {
                let data = await res.json();
                console.log("result data:", data);
                // fetch(`http://127.0.0.1:8080/?url=${data["url"]}`);
                setRelated(data["related"]);
                setMore(data["more"]);
            }
            else {
                alert("cannot resolve the query")
                console.error("error");
            }
        }
        fn();
    }, [item]);
    return (
        <div className={Styles.ResultContainer}>
            
            <div>
                <span>
                    
                more stuff
                </span>
            </div>
            <div>
                <span>

                Result for {item}
                </span>
            </div>
            <div>
                <span>

                related stuff
                </span>
            </div>
        </div>

    )
}

export default ResultPage;
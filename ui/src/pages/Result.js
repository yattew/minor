
import { useContext, useEffect, useState } from "react";
import ResultMore from "../components/ResultMore";
import ResultRelated from "../components/ResultRelated"
import Styles from "../css/result.module.css"
import config from "../config"
import { openInNewWin } from "../utils";
import { useParams } from "react-router-dom";
import LearningModeContext from "../Contexts";

const ResultPage = () => {
    const { item } = useParams();
    const {mode} = useContext(LearningModeContext);
    const [results, setResults] = useState([]);
    const [related, setRelated] = useState([]);
    useEffect(() => {
        console.log("from result page:", item);
        const fn = async () => {
            let query = item;
            let host_addr = config.host_addr;
            let res = await fetch(host_addr + "result/" + query + "/" + mode);
            if (res.ok) {
                let data = await res.json();
                console.log("result data:", data);
                // fetch(`http://127.0.0.1:8080/?url=${data["url"]}`);
                setResults(data["urls"]);
                setRelated(data["related"]);
            }
            else {
                alert("cannot resolve the query")
                console.error("error");
            }
        }
        fn();
    }, [item, mode]);
    const openInNewWin = (url) => {
        fetch(`http://127.0.0.1:8080/?url=${url}`);
    }
    return (
        <div className={Styles.ResultContainer}>
            <div className={Styles.ResultMain}>
                <div>
                    Result for {item}
                </div>
                <ul>
                    {
                        results.map((el) => {
                            return <li className={Styles.ResultListItem} key={el["title"]}>
                                <div>
                                    <div>
                                        <div className={Styles.ResultTitle}>
                                            <span className={
                                                Styles.Difficulty +
                                                " "
                                                +
                                                (el["difficulty"] == "beginner" ?
                                                    Styles.green
                                                    :
                                                    (el["difficulty"] == "intermediate" ?
                                                        Styles.yellow
                                                        :
                                                        Styles.red))
                                            }>
                                                {"[  " + el["difficulty"] + "  ]  "}
                                            </span>
                                            {el["title"].substr(0, 80)}

                                        </div>
                                        <div>

                                            <a href={el["url"]} onClick={(e) => { e.preventDefault() }}>
                                                {el["url"].substr(0, 80)}
                                            </a>
                                        </div>
                                    </div>
                                    <button
                                        className="btn btn-primary"
                                        onClick={() => openInNewWin(el["url"])}
                                    >
                                        open
                                    </button>
                                </div>
                            </li>
                        })
                    }
                </ul>
            </div>
            <div className={Styles.ResultRelated}>
                <div>
                    related stuff
                </div>
            </div>
        </div>

    )
}

export default ResultPage;
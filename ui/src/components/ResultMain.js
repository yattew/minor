import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import config from "../config";


const ResultMain = () => {
    const [ doc, setDoc ] = useState("");
    const {item} = useParams();
    useEffect(() => {
        let addr = config.host_addr;
        const fn = async () => {
            let res = await fetch(`${addr}/doc/${item}`);
            let data = await res.json();
            let doc = data["doc"];
            setDoc(doc);
        }
        fn();
    }, [item]);
    return (
        <div>
            
            {/* This is the main result {item} */}
        </div>
    )
}

export default ResultMain;
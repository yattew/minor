import { useState } from "react";
import config from "../config";
import SearchResult from "./SearchResult";
import Styles from "../css/search.module.css";
const Search = () => {
    const [searchResults, setSearchResults] = useState([]);
    const handleChange = async (e) => {
        let query = e.target.value;
        let host_addr = config.host_addr;
        let res = await fetch(host_addr + "query/" + query);
        if (res.ok){
            let data = await res.json();
            console.log(data);
            setSearchResults(data["res"]);
        }
        else{
            setSearchResults([]);
        }
    }
    return (
        <>
            <div className={Styles.searchContainer}>

                <input className="form-control" onKeyUpCapture={handleChange} type="search" placeholder="Search" />
                {
                    searchResults.length ?
                        <div className={Styles.searchResultContainer}>
                            {searchResults.map((item) => <SearchResult item={item} key={item}/>)}
                        </div>
                        : null
                }
            </div>
        </>
    );
}

export default Search;
import { useRef, useState } from "react";
import config from "../config";
import SearchResult from "./SearchResult";
import Styles from "../css/search.module.css";
const Search = () => {
    const [searchResults, setSearchResults] = useState([]);
    const inputRef = useRef();
    const handleChange = async (e) => {
        let query = e.target.value;
        let host_addr = config.host_addr;
        let res = await fetch(host_addr + "query/" + query);
        if (res.ok) {
            let data = await res.json();
            console.log(data);
            setSearchResults(data["res"]);
        }
        else {
            setSearchResults([]);
        }
    }
    const clearSearch = () => {
        setSearchResults([]);
        inputRef.current.value = "";
    }
    const currSearchVal = () => {
        return inputRef.current?.value;
    }
    return (
        <>
            <div className={Styles.searchContainer}>

                <input className="form-control" onKeyUpCapture={handleChange} type="search" placeholder="Search" ref={inputRef} />
                {
                    currSearchVal() ?
                        <div className={Styles.searchResultContainer}>
                            <SearchResult show={"search for: " + currSearchVal()} item={currSearchVal()} clearSearch={clearSearch} />
                            {
                                searchResults.map((item) => <SearchResult show={item} item={item} key={item} clearSearch={clearSearch} />)
                            }
                        </div>
                        : null
                }
                
            </div>
        </>
    );
}

export default Search;
import { useNavigate } from "react-router-dom";

const SearchResult = ({ item, clearSearch }) => {
    const navigate = useNavigate();
    console.log("here", item);
    const handleClick = () => {
        clearSearch();
        navigate(`/result/${item}`);
    }
    return (
        <div onClick={handleClick}>{item}</div>
    )
}

export default SearchResult;
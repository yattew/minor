import { useNavigate } from "react-router-dom";
const SearchResult = ({ show, item, clearSearch }) => {
    const navigate = useNavigate();
    const handleClick = () => {
        clearSearch();
        navigate(`/result/${item}`);
    }
    return (
        <div onClick={handleClick}>{show}</div>
    )
}

export default SearchResult;
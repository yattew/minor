import styles from "../css/SearchPage.module.css"
const SearchPage = () => {
    return (
        <div className={styles.searchContainer}>
            <input className="form-control" placeholder="active search"></input>
        </div>
    );
}

export default SearchPage;
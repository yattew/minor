import styles from "../css/navbar.module.css";
import Search from "./Search";
const Navbar = () => {
    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <div className={styles.navContent}>
                <div className={styles.leftContent}>
                    <div className="navbar-brand">Python-Help</div>
                </div>
                <Search/>
                <div className={styles.rightContent}>
                    <button className="btn btn-primary">Help</button>
                </div>
            </div>
        </nav>
    );
}

export default Navbar;
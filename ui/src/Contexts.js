const { createContext, useState } = require("react");

const LearningModeContext = createContext()
export default LearningModeContext;

let  modes = {
    "video":"video",
    "reading":"reading",
    "practice":"practice",
}


export const LearningModeProvider = ({children})=>{
    const [mode, setMode] = useState(modes.video);
    return (
        <LearningModeContext.Provider value={{mode, setMode, modes}}>
            {children}
        </LearningModeContext.Provider>
    )
}
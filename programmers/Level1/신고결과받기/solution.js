function solution(idList, report, k) {
    const answer = [];
    const reportInfoObj = {};
    
    idList.forEach((id, index) => {
        answer[index] = 0;
        reportInfoObj[id] = {mailCount:0, reportTargetList:[], reportedCount:0};
    });
    report.forEach(reportPair => {
        const [reporterId, reportedId] = reportPair.split(' ');
        if (!reportInfoObj[reporterId].reportTargetList.includes(reportedId)) {
            reportInfoObj[reportedId].reportedCount++;
            reportInfoObj[reporterId].reportTargetList.push(reportedId);
        }
    });
    idList.forEach((id, index) => {
        const reportTargetList = reportInfoObj[id].reportTargetList;
        reportTargetList.forEach(reportedId => {
            const reportedCount = reportInfoObj[reportedId].reportedCount;
            if (reportedCount >= k) {
                answer[index]++;
            }
        });
    });
    return answer;
}